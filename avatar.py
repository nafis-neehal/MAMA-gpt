import subprocess

# Replace these with your actual file paths or variables that contain the paths
checkpoint_path = "checkpoints/wav2lip_gan.pth"
face_video_path = "trump.mp4"
audio_source_path = "q1.wav"

# Construct the command as a list of arguments
cmd = [
    "python", "inference.py",
    "--checkpoint_path", checkpoint_path,
    "--face", face_video_path,
    "--audio", audio_source_path
] 

print("Generating Avatar...")

# Run the command
result = subprocess.run(cmd, capture_output=True, text=True)

# Check if the command was executed successfully
if result.returncode == 0:
    print("Generated Avatar successfully.")
    print("Output:", result.stdout)
else:
    print("Error in generating avatar.")
    print("Error:", result.stderr)
