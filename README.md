## Inspiration

So the idea of building such a project came from the fact that how ruthless we humans are in consuming the resources provided to us by nature. One such important resource is **water**.

Water is being wasted and polluted so much, that it is happening at a rate that we never imagined. So we decided to build a project which monitors the water consumption, the cleanliness of the water being thrown out, etc. and charges accordingly.

A very important thing to be noted here is that about water tampering which is a common problem across all over the world. With the implementation of blockchain on timely basis, we not only prevent people from unfair practices but also generate a credit distribution system to motivate them to take their steps in conservation of this precious resource and utilize them wisely.

> And guess what?\
> It record all this data on a blockchain, so it never alters once recorded!

## What it does?

### The project basically does the following things:

- Take input from the camera, set on the flow of the water.
- Analyze the flow rate of water in `square pixels/frame` and measure the volume consumed.
- Accordingly measure the Performance Index, Flow Credits, etc.
- Record all these value onto the blockchain so it's immutable.
- Prevent any kind of _tampering_ by water industries and _monitor_ the water in efficient way and hence motivate them to follow the best practice and conserve water.
- Based on the consumption, the credit will be distributed to the consumers, which will motivate and help them consume the water resources in efficient and non-destructing manner.

## How we built it

> - The main function of real world observation is implemented through **OpenCV** using a camera. In the given code, we have implemented our project using pre-recorded video but that can be easily altered by changing the statement:
> cam=cv2.VideoCapture("videoname.mp4") 
to
> cam=cv2.VideoCapture(0) #Or whatever external cam is being used

![OpenCV Working](https://github.com/sedhha/blocksquid/blob/master/graphicfiles/background.gif)

> - A very simple blockchain protocol is being implemented in Python for simplicity and learning friendly approach.


### This is how it works:

- `WatertypeDetermination.py` => A code to create histograms which then
will help in colour comparision. Add the path for cropped images of fresh water and waste water
- `WaterClassifier.py` => Necessary functions to execute water quality and flow rate.

![Flow Demo - OpenCV](https://github.com/sedhha/blocksquid/blob/master/graphicfiles/demo4.gif)
![Pixel Variation - OpenCV](https://github.com/sedhha/blocksquid/blob/master/graphicfiles/pixelvariation.gif)

- `blockchain.py` => File to start mining block
- `blockchainv0.py` => V0 of `blockchain.py`
- `codetodetectflowrate.py` => Press R to print selectedROI (while running the program) and some other variables code has all the explanation for the same

![ROI1](https://github.com/sedhha/blocksquid/blob/master/graphicfiles/selectroi.jpg)
![ROI2](https://github.com/sedhha/blocksquid/blob/master/graphicfiles/selectROI2.jpg)

## Challenges we ran into

> ### Major challenges we faced:
>
> - Reading the real world data i.e. _hardware -> software_
> - Writing the data to the blockchain accordingly by averaging out values.
> - Attempting to implement the NEAR API in our project. 

## Accomplishments that we're proud of

> We're proud of the implementation that we did for writing the data from the hardware to the blockchain directly

## What we learned

- The major learning from this project we had, is the blockchain part. We learn how a blockchain can seamlessly integrate with the hardware and software as required.

## What's next for BlockSquid

> Further we would like to add more features such as a administrative dashboard, cost calculation and improve the throughput calculation.

## References

> - [Blockchain Demo (https://github.com/anders94/blockchain-demo/)](https://github.com/anders94/blockchain-demo/)
> - [Blockchain A-Z™](https://www.superdatascience.com/pages/blockchain)
> - [w3schools](https://www.w3schools.com/)
