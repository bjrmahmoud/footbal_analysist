from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS  # For enabling CORS
from utils import read_video, save_video
from trackers import Tracker
import os
import time

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Temporary folders for saving uploaded videos
UPLOAD_FOLDER = 'temp'
OUTPUT_FOLDER = 'output_videos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')  # Serve index.html (optional)

@app.route('/process_video', methods=['POST'])
def process_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file provided'}), 400

    video_file = request.files['video']
    video_path = os.path.join(UPLOAD_FOLDER, video_file.filename)
    video_file.save(video_path)

    try:
        start_time = time.time()  # Start time for processing
        output_path = os.path.join(OUTPUT_FOLDER, f'processed_{video_file.filename}')
        process_and_save_video(video_path, output_path)
        end_time = time.time()  # End time for processing

        processing_time = end_time - start_time
        print(f"Video processed in {processing_time} seconds")

        return jsonify({
            'message': 'Video processed successfully',
            'output_path': f'/output_videos/processed_{video_file.filename}'  # URL to processed video
        }), 200
    except Exception as e:
        return jsonify({'error': f'Processing failed: {str(e)}'}), 500

def process_and_save_video(input_path, output_path):
    video_frames = read_video(input_path)
    tracker = Tracker('models/best.pt')

    # Get object tracks
    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='stubs/track_stubs.pkl')

    # Draw object tracks on frames
    output_video_frames = tracker.draw_annotations(video_frames, tracks)

    # Save the processed video
    save_video(output_video_frames, output_path)

@app.route('/output_videos/<filename>')
def serve_video(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
