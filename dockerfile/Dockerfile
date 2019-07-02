FROM nvidia/cuda:9.0-cudnn7-devel
LABEL maintainer="Todor Stoyanov"

# 0 installing CUDA all the way
WORKDIR /
#Installing Python, Jupyter, Tensorflow, OpenAI Gym
###################################################
# 1. installing python2 and python3
RUN apt-get update && \
	apt install -y --no-install-recommends python3-pip python-pip python3 python
# 1.1 uppgrade pip and pip3
RUN pip3 install --upgrade pip setuptools && pip install --upgrade pip

# 2. installing jupyter, and a bunch of Science Python Packages
# packages taken from https://hub.docker.com/r/jupyter/datascience-notebook/
# RUN pip3 install jupyter pandas matplotlib scipy seaborn scikit-learn scikit-Image sympy cython patsy statsmodels cloudpickle dill numba bokeh

# 3. installing Tensorflow (GPU)
# see here https://www.tensorflow.org/install/install_linux#InstallingNativePip
RUN pip3 install tensorflow-gpu==1.3.0

# TODO MAKE SURE IT IS >= 1.3, possibly test
# RUN pip3 install tensorflow==1.3.0

#ES# 5. installing dependencies for Tangent Convolution
RUN pip3 install joblib

# TensorBoard
EXPOSE 6006
# IPython
EXPOSE 8888
# VNC Server
EXPOSE 5900


CMD mkdir Student
CMD cd Student

# Open3D
CMD git clone https://github.com/tatarchm/Open3D.git

# Build
CMD cd Open3D
CMD util/scripts/install-deps-ubuntu.sh
CMD mkdir build
CMD cd build
CMD cmake ../src
CMD make

# Tangent Convolution
CMD cd ..
CMD cd ..
CMD git clone https://github.com/martine94/SummerInternship.git
CMD cd SummerInternship

# Get Semantic3D dataset 
CMD python get_data.py inputFiles outputFiles semantic3d

# Precompute 
# CMD python tc.py experiments/semantic3d/dhnrgb/config.json --precompute

# CMD python tc.py experiments/semantic3d/dhnrgb/config.json --train


# 4. installing X and xvfb so we can SEE the action using a remote desktop access (VNC)
# and because this is the last apt, let's clean up after ourselves
RUN apt-get update && apt-get install -y vim python-opengl python3-opengl
RUN apt-get install -y x11vnc xvfb fluxbox wmctrl && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/* && \
		rm -rf /cudnn-8.0-linux-x64-v7.tgz && \
		rm -rf /cuda/

COPY run.sh /
CMD ["/run.sh", "--allow-root"]
