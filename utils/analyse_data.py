import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

filename = "box2_DEFAULT_T46.csv"
filepath = fr"C:\Users\vedan\Desktop\project\data\raw\initial data\{filename}"

df = pd.read_csv(filepath)
COLUMNS = ['Timestamp', 'Pelvis_extension', 'Pelvis_lateral_flexion_rotation',
       'Pelvis_axial_rotation', 'LeftHip_flexion', 'LeftHip_adduction',
       'LeftHip_external_rotation', 'LeftKnee_flexion', 'LeftKnee_adduction',
       'LeftKnee_external_rotation', 'LeftAnkle_dorsiflexion',
       'LeftAnkle_inversion', 'LeftAnkle_internal_rotation',
       'RightHip_flexion', 'RightHip_adduction', 'RightHip_external_rotation',
       'RightKnee_flexion', 'RightKnee_adduction',
       'RightKnee_external_rotation', 'RightAnkle_dorsiflexion',
       'RightAnkle_inversion', 'RightAnkle_internal_rotation',
       'Thorax_extension', 'Thorax_lateral_flexion_rotation',
       'Thorax_axial_rotation', 'LeftScapula_protraction',
       'LeftScapula_medial_rotation', 'LeftScapula_posterior_tilt',
       'LeftShoulder_flexion', 'LeftShoulder_abduction',
       'LeftShoulder_external_rotation', 'LeftElbow_flexion',
       'LeftElbow_abduction', 'LeftElbow_pronation', 'LeftWrist_flexion',
       'LeftWrist_abduction', 'LeftWrist_pronation', 'Neck_flexion',
       'Neck_left-ward_tilt', 'Neck_right-ward_rotation',
       'RightScapula_protraction', 'RightScapula_medial_rotation',
       'RightScapula_posterior_tilt', 'RightShoulder_flexion',
       'RightShoulder_abduction', 'RightShoulder_external_rotation',
       'RightElbow_flexion', 'RightElbow_abduction', 'RightElbow_pronation',
       'RightWrist_flexion', 'RightWrist_abduction', 'RightWrist_pronation']

#body_joint = df.LeftKnee_flexion

#print("Contents in csv file:", df)
#print(df.columns)
plt.plot(df.LeftShoulder_flexion, label = "Left_Elbow")
plt.plot(df.RightShoulder_flexion, label ="Right_Elbow")
plt.plot(df.LeftKnee_flexion, label = "LeftKnee_flexion")
plt.plot(df.RightKnee_flexion, label = "RightKnee_flexion")
plt.title(f"{filename}:joint angles")
plt.xlabel("Time")
plt.ylabel("Degrees")
plt.grid(True)
plt.legend()
plt.show()