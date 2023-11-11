import os, tensorflow, keras

base_model = VGG16()
image_model = Model(inputs=base_model.inputs(), outputs=base_model.layers[-2].output())

