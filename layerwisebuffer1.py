import numpy as np
image_size = 8
kernel_size = 3
stride = 2
channel_number = 256  # Assuming RGB image
layers=22
image_matrix = np.random.randint(low=-128, high=127, size=(image_size, image_size, channel_number), dtype=np.int8)
output_size = ((image_size - kernel_size) // stride) + 1
def calculate_layer_buffer_size(input_shape, kernel_size, stride):
    output_size = ((input_shape - kernel_size) // stride) + 1
    return output_size * output_size * channel_number
total_buffer_size = 0
for layer in range(layers):
    layer_buffer_size = calculate_layer_buffer_size(image_size, kernel_size, stride)
    total_buffer_size += layer_buffer_size

    # Print buffer size for the current layer
    print(f"Buffer size for Layer {layer + 1}: {layer_buffer_size}")

# Print total buffer size
print(f"Total Buffer Size: {total_buffer_size}")

# Function to perform convolution with given kernel and stride
def convolution(image, kernel_size, stride):
    result_matrix = []
    for i in range(0, image_size - kernel_size + 1, stride):
        row_result = []
        for j in range(0, image_size - kernel_size + 1, stride):
            # Extract the kernel
            kernel = image[i:i+kernel_size, j:j+kernel_size]
            # Perform some operation with the kernel (for example, averaging)
            # Here, we'll just flatten the kernel into a list
            flattened_kernel = kernel.flatten()
            row_result.append(flattened_kernel)
        result_matrix.append(row_result)
    return np.array(result_matrix, dtype=object)

# Perform convolution
result_matrix = convolution(image_matrix, kernel_size, stride)

# Print the original image matrix
print("\nOriginal Image Matrix:")
print(image_matrix)

# Print the result matrix after convolution
print("\nResult Matrix after Convolution:")
print(result_matrix)

# Print the output size
print("\nOutput Size:", output_size)
