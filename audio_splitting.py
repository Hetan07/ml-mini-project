import pydub
from pydub import AudioSegment
import feature_extraction
import io
def split_audio(uploaded_file):
    # Load your audio file
    # audio = AudioSegment.from_file("classical.00000.wav", format="wav")
    audio = AudioSegment.from_file(uploaded_file,)
    # Define the duration of each segment in milliseconds (3 seconds)
    segment_duration = 3 * 1000  # 3 seconds in milliseconds

    # Check the total duration of the audio
    audio_duration = len(audio)

    # Check if the audio is shorter than 1 minute and 3 seconds
    if audio_duration < 63 * 1000:
        # If it's shorter, take audio from 0 to 3 seconds
        segment = audio[:segment_duration]
    else:
        # If it's longer, take audio from 1 minute to 1 minute 3 seconds
        start_time = 60 * 1000  # 1 minute in milliseconds
        end_time = start_time + segment_duration
        segment = audio[start_time:end_time]
    output_stream = io.BytesIO()
    segment.export(output_stream, format="wav")

    # Now you can directly use the output_stream for feature extraction
    output_stream.seek(0)  # Reset the stream position to the beginning

    # Process and extract features from the segment
    features = feature_extraction.all_feature_extraction(output_stream)

    return features
# output_file = "D:/miniproject/output_segment.wav"

# Save the segment to a new file
# segment.export(output_file, format="wav")
