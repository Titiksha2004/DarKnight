import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    frame = cv2.flip(frame, 1)  

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    light_intensity = np.mean(gray)

    equalized = cv2.equalizeHist(gray)

    night_vision_frame = cv2.merge((np.zeros_like(equalized), equalized, np.zeros_like(equalized)))

    night_vision_frame = cv2.convertScaleAbs(night_vision_frame, alpha=1.5, beta=30)

    intensity_text = f"Light Intensity: {int(light_intensity)}"
    cv2.putText(night_vision_frame, intensity_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    if light_intensity > 150: 
        warning_text = "Too Much Light!"
        cv2.putText(night_vision_frame, warning_text, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    
    cv2.imshow('Night Vision', night_vision_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
