#In this code we have assumed same padding and stride, each convolutional layer reduces spatial dimensions by 2
def max_buffer(input_shape, num_layers=10, filters=256, kernel_size=3):
    buffer_size = input_shape[0] * input_shape[1] * input_shape[2]  # Initial buffer size
    for _ in range(num_layers):
        input_shape = (
            max(1, input_shape[0] // 2),
            max(1, input_shape[1] // 2),
            filters
        )
        num_params = filters * kernel_size * kernel_size * input_shape[2] #number of parameters in convolutional layer
        buffer_size += input_shape[0] * input_shape[1] * input_shape[2] #Add the buffer size of the layer
    return buffer_size
input_shape = (227,227,256)  #Input shape (height, width, channels)
max_buffer_size = max_buffer(input_shape)
print(f"Max Buffer Size: {max_buffer_size} elements")
