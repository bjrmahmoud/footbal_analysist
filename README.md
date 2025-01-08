# ⚽ GoalLens - Phase 2 : Football Analysis Web Project

Welcome to the **GoalLens Analysis Project - Phase 2**!This project is designed to analyze football videos by detecting and tracking players, referees, and the football itself, using advanced AI and computer vision techniques.

**Phase 0** focuses on detecting and tracking key objects in football videos, including players, referees, and the football itself, using YOLO. Additional features include team assignment based on t-shirt colors, ball acquisition analysis, player movement tracking, and speed calculation. This phase is crucial for ensuring the core functionality of the analysis system.

For more details on **Phase 0**, check out the [Phase 0 repository](https://github.com/Imane-Bjr/goalLens-model).

**Phase 2** was added to make it easier to create an API that can later be integrated with a mobile app built with **Flutter**. This phase ensures that the core video processing functionality can be accessed via an API, making it more efficient and scalable for mobile use. Additionally, it addresses the concern of avoiding high costs when deploying on platforms like **Azure**, as this phase prepares the system to run seamlessly on a mobile app without incurring extra charges for cloud-based deployments.


---

## 📂 Project Structure

Here's an organized breakdown of the project's folder hierarchy:

- **`input_video/`**: This is where you upload your raw football video files for processing.
- **`models/`**: Stores pre-trained YOLO models like `best.pt` used for detection and tracking.
- **`output_videos/`**: All processed video outputs are saved here for easy access.
- **`runs/`**: Contains the results of different detection runs. Includes subfolders like `predict/` and `predict2/` for various sets of predictions.
- **`stubs/`**: Holds temporary data used for testing the tracking system, such as stub files (`track_stubs.pkl`).
- **`temp/`**: A temporary folder where uploaded files are stored before processing.
- **`templates/`**: Includes the HTML templates used by the Flask web application.
- **`trackers/`**: Contains the logic for tracking players, referees, and footballs in the video. Includes necessary Python files.
- **`training/`**: Holds the training, validation, and test datasets for YOLO object detection training.
- **`utils/`**: Utility functions for handling tasks like reading and saving video files.
- **`Scripts/`**: Various scripts used for running processes or assisting with analysis tasks.
- **`share/`**: Shared resources for things like Jupyter kernels and man pages.

---

This structure ensures that each component of the project has its own place, making the project easier to maintain, scale, and collaborate on. Let me know if you'd like to add or modify any sections!

## 🚀 Features

- **Real-Time Detection & Tracking**: Detect and track players, referees, and the football using a YOLO-based model.
- **Team Classification**: Assign players to teams based on jersey colors using pixel clustering.
- **Speed and Movement Analysis**: Measure players' speed, distance, and movements using optical flow and perspective transformation.
- **Web Interface**: Interact with the application through an intuitive Flask-based web interface.

---

## 🚀 How to Run

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/your-username/football_analysis.git
cd football_analysis
```

### 2. Install Dependencies

You need to install the necessary dependencies. First, ensure you have Python 3.8 or higher. Then, run the following command to install required libraries:

```bash
pip install -r requirements.txt
```

### 3. Run the Flask Application
Run the Flask app with the following command:

```bash
python main.py
```
This will start the web server on http://localhost:5000.

### 4. Access the Application
After running the Flask app, open your browser and go to:
http://localhost:5000
You should be able to upload videos and see the results after processing.

## 🛠 Dependencies

Ensure the following dependencies are installed:

- **Python 3.8+**
- **Flask**: For the web framework
- **Flask-CORS**: For enabling Cross-Origin Resource Sharing
- **OpenCV**: For video processing and object detection
- **Other packages** listed in `requirements.txt` (or manually installed using `pip`)

---

## 🌟 Future Enhancements

- Implement advanced AI techniques for tactical insights.
- Integrate a dashboard for live match statistics.
- **Reduce cloud deployment costs**: By preparing the system for API integration, we can avoid the costs associated with cloud platforms like **Azure** while still providing full functionality for mobile users.

---

## 📷 Example Output

![Example Output](static/assets/output.png)

---

## 🤝 Contributing

We welcome contributions to this project! Feel free to fork the repo and submit pull requests.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 📧 Contact

If you have any questions or need further assistance, feel free to reach out:

- **Email:** boujirimane1@gmail.com
- **GitHub:** https://github.com/Imane-Bjr