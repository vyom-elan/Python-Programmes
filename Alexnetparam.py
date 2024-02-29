#Alexnet
#In this code we have assumed same padding and stride.
'''filter_dim = kernel size(has to be an odd number)
   input_channel = number of channels for an input of an image
   numfilt= number of filters in the given convolutional layer(for example in the first convolutional layer there are 96 layers)'''
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