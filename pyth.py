from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('_ICF9BgFjuLYx6GSx7luNeeVUYy2ChzF65lNiHdT_1cK')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/6382eb61-3ceb-4c38-9eb0-d6c898b87a20')

with open('hello_world.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'Hello world',
            voice='en-US_MichaelV3Voice',
            accept='audio/wav'        
        ).get_result().content)