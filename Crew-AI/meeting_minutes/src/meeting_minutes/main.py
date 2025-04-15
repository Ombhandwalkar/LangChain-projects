from pydantic import BaseModel
from crewai.flow.flow import Flow,listen,start
from pydub import AudioSegment
from pydub.utils import make_chunks
from pathlib import Path
from crewai import LLM
from crews.meeting_minutes_crew.meeting_minutes_crew import MeetingMinutesCrew
from crews.gmailcrew.gmailcrew import GmailCrew

import agentops
import os 
from dotenv import load_dotenv
load_dotenv()


client=LLM(
    model='ollama/mistral',
    base_url='http://localhost:11434',
    timeout=5000
)

class MeetingMinutesState(BaseModel):
    transcript:str=''
    meeting_minutes:str=''


class MeetingMinutesFlow(Flow[MeetingMinutesState]):
    @start
    def transcribe_meeting(self):
        print('Generating Transcription')

        SCRIPT_DIR=Path(__file__).parent
        audio_path=str(SCRIPT_DIR/'EarningsCall.wav')

        # Load the audio file 
        audio=AudioSegment.from_file(audio_path,format='wav')

        chunk_length_ms=60000
        chunks=make_chunks(audio,chunk_length_ms)

        # Transcribe each chunk
        full_transcription=''
        for i ,chunk in enumerate(chunks):
            print(f"Transcribing chunks{i+1}/{len(chunks)}")
            chunk_path=f"chunk_{i}.wav"
            
            with open(chunk_path,'rb')as audio_file:
                transcription=client.audio.transcription.create(
                    model='whisper-1',
                    file=audio_file
                )
                full_transcription +=transcription.text+" "

        self.state.transcript=full_transcription
        print(f"Transcription:{self.state.transcript}")


    @listen(transcribe_meeting)
    def generate_meeting_minutes(self):
        print('Generating Meeting minutes')

        crew=MeetingMinutesCrew()

        inputs={
            'transcript':self.state.transcript
        }
        meeting_minutes=crew.crew().kickoff(inputs)
        self.state.meeting_minutes=meeting_minutes

    @listen(generate_meeting_minutes)
    def create_draft_meeting_minutes(self):
        print("Creating Draft Meeting Minutes")

        crew = GmailCrew()

        inputs = {
            "body": self.state.meeting_minutes
        }

        draft_crew = crew.crew().kickoff(inputs)
        print(f"Draft Crew: {draft_crew}")

def kickoff():
    session = agentops.init(api_key=os.getenv("AGENTOPS_API_KEY"))

    meeting_minutes_flow = MeetingMinutesFlow()
    meeting_minutes_flow.plot()
    meeting_minutes_flow.kickoff()

    session.end_session()

if __name__ == "__main__":
    kickoff()