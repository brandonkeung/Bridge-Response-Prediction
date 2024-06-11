# import matlab.engine

# # Start MATLAB engine
# eng = matlab.engine.start_matlab()

# # Add the directory containing the MATLAB script to MATLAB's path
# eng.addpath(r'/path/to/matlab/script/directory')

# # Import the MATLAB script
# import CB_2014_nga_revised

# # Call the MATLAB function
# CB_2014_nga_revised.CB_2014_nga_revised(nargout=0)  # Provide inputs as necessary

# # Stop MATLAB engine
# eng.quit()

import scipy.io
mat = scipy.io.loadmat('CB14_Consts.mat')
print(mat)