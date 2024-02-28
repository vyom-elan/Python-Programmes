import numpy as np
image_size = 8
kernel_size = 3
stride = 2  
channel_number = 3  # Assuming RGB image
layers=22    
# Create an 8x8x3 image matrix with random int8 values
image_matrix = np.random.randint(low=-128, high=127, size=(image_size, image_size, channel_number), dtype=np.int8)
# Calculate output size
output_size = ((image_size - kernel_size) // stride) + 1
# Function to calculate buffer size for each layer
def calculate_layer_buffer_size(input_shape, kernel_size, stride):
    output_size = ((input_shape - kernel_size) // stride) + 1
    return output_size * output_size * channel_number
total_buffer_size = 0
# Iterate over layers to calculate buffer size
for layer in range(layers):
    layer_buffer_size = calculate_layer_buffer_size(image_size, kernel_size, stride)
    total_buffer_size += layer_buffer_size
    # Print buffer size for the current layer
    print(f"Buffer size for Layer {layer + 1}: {layer_buffer_size}")# Print total buffer size
print(f"Total Buffer Size: {total_buffer_size}")
# Function to perform convolution with given kernel and stride
def convolution(image, kernel_size, stride):
    result_matrix = []
    for i in range(0, image_size - kernel_size + 1, stride):
        row_result = []
        for j in range(0, image_size - kernel_size + 1, stride):
            kernel = image[i:i+kernel_size, j:j+kernel_size]#Extraction of kernel
            flattened_kernel = kernel.flatten()
            row_result.append(flattened_kernel)
        result_matrix.append(row_result)
    return np.array(result_matrix, dtype=object)
result_matrix = convolution(image_matrix, kernel_size, stride)
print("\nOriginal Image Matrix:")
print(image_matrix)
print("\nResult Matrix after Convolution:")
print(result_matrix)
print("\nOutput Size:", output_size)
def parametrs_conv(filter_dim, input_channel, numfilt):
    convlayer=1
    filter_dim=5
    input_channel=3
    for convlayer in range(1, 6):
        if convlayer == 1:
            #filter_dim=11
            numfilt=96
            num_param = (filter_dim * filter_dim * input_channel + 1) * numfilt
        elif convlayer == 2:
            #filter_dim=5
            numfilt=256
            num_param = (filter_dim * filter_dim * input_channel + 1) * numfilt
        elif convlayer == 3:
            #filter_dim=3
            numfilt=384
            num_param = (filter_dim * filter_dim * input_channel + 1) * numfilt
        elif convlayer == 4:
            #filter_dim=3
            numfilt=384
            num_param = (filter_dim * filter_dim * input_channel + 1) * numfilt
        elif convlayer == 5:
            #filter_dim=3
            numfilt=256 
            num_param = (filter_dim * filter_dim * input_channel + 1) * numfilt
            return num_param
        input_channel=numfilt
        convlayer=convlayer+1
        print("Number of parameters", num_param)
filter_dim=1    #to initialise the parameter for the function 
input_channel=1 #to initialise the parameter for the function
numfilt=1       #to initialise the parameter for the function   
result=parametrs_conv(filter_dim, input_channel, numfilt)
print(result) 
