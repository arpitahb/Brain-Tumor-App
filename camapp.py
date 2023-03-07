import streamlit as st
from PIL import Image
img1=Image.open("C:\\Users\\JEC\\SL2\\venv\\eyecatch1.jpg")
st.image(img1, width=800)
st.header("Brain Tumor Detection")
st.write("Try uploading an MRI and watch our model detect the possibility of a brain tumor in the upload image")

with st.sidebar:
  img=Image.open("C:\\Users\\JEC\\SL2\\venv\\imagebrain.jfif")
  st.image(img)
  st.subheader("How Does This App Work?")
  st.write("A brain tumor is understood by the scientific community as the growth of abnormal cells in the brain, some of which can lead to cancer. The traditional method to detect brain tumors is nuclear magnetic resonance (MRI). Having the MRI images, information about the uncontrolled growth of tissue in the brain is identified. In several research articles, brain tumor detection is done through the application of Machine Learning and Deep Learning algorithms. When these systems are applied to MRI images, brain tumor prediction is done very quickly and greater accuracy helps to deliver treatment to patients. These predictions also help the radiologist to make quick decisions. In the proposed work, a set of Artificial Neural Networks (ANN) are applied in the detection of the presence of brain tumor, and its performance is analyzed through different metrics.")

s= st.camera_input(label="Upload you Image", label_visibility="visible")
submit=st.button(label="Check for Brain tumor?")
if submit:
    st.subheader("Output")
    with st.spinner(text="This may take a moment..."):
      st.write("Your are/are not suffering from tumor")