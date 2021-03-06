# Copyright (c) 2019 NVIDIA Corporation
import nemo

# instantiate Neural Factory with supported backend
nf = nemo.core.NeuralModuleFactory()

# instantiate necessary neural modules
dl = nemo.tutorials.RealFunctionDataLayer(
    n=10000, batch_size=128)
fx = nemo.tutorials.TaylorNet(dim=4)
loss = nemo.tutorials.MSELoss()

# describe activation's flow
x, y = dl()
p = fx(x=x)
lss = loss(predictions=p, target=y)

# SimpleLossLoggerCallback will print loss values to console.
callback = nemo.core.SimpleLossLoggerCallback(
    tensors=[lss],
    print_func=lambda x: print(f'Train Loss: {str(x[0].item())}'))

# Invoke "train" action
nf.train([lss], callbacks=[callback],
         optimization_params={"num_epochs": 3, "lr": 0.0003},
         optimizer="sgd")
