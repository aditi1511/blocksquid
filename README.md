## Inspiration

So the idea of building such a project came from the fact that how ruthless we humans are in consuming the resources provided to us by nature. One such important resource is **water**.

Water is being wasted and polluted so much, that it is happening at a rate that we never imagined. So we decided to build a project which monitors the water consumption, the cleanliness of the water being thrown out, etc. and charges accordingly.

> And guess what?\
> It record all this data on a blockchain, so it never alters once recorded!

## What it does?

### The project basically does the following things:

- Take input from the camera, set on the flow of the water.
- Analyze the flow rate of water in `cubic pixels/sec` and measure the volume consumed.
- Accordingly measure the Performance Index, Flow Credits, etc.
- Record all these value onto the blockchain so it's immutable.

## How we built it

> The main function of real world observation is implemented through **OpenCV** using a camera.

![OpenCV Working](/blocksquid/graphicfiles/background.gif)

### This is how it works:

- `WatertypeDetermination.py` => Add the path for cropped images of fresh water and waste water
- `WaterClassifier.py` => Necessary functions to execute water quality and flow rate

![Flow Demo - OpenCV](/blocksquid/graphicfiles/demo4.gif)
![Pixel Variation - OpenCV](/blocksquid/graphicfiles/pixelvariation.gif)

- `blockchain.py` => File to start mining block
- `blockchainv0.py` => V0 of `blockchain.py`
- `codetodetectflowrate.py` => Press R to print selectedROI (while running the program) and some other variables code has all the explanation for the same

![ROI1](/blocksquid/graphicfiles/selectroi.jpg)
![ROI2](/blocksquid/graphicfiles/selectROI2.jpg)

## Challenges we ran into

> ### Major challenges we faced:
>
> - Reading the real world data i.e. _hardware -> software_
> - Writing the data to the blockchain accordingly by averaging out values.
> - Implementing the NEAR API in our project.

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
