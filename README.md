# AR2-D2:Training a Robot Without a Robot

## Processing pipeline for data modelities via AR2-D2 collected Data

![ezgif com-video-to-gif (8)](https://github.com/jiafei1224/AR2-D2_Utils/assets/51585075/a3d72d1f-460e-4a2e-a679-522c14054e31)

## Process 2D robot data
It is created using **RGB video data** for training visumotor policies, using the RGB data extracted from AR2-D2 interface.

#### 1. Detectron2DeepSortPlus

AR2-D2 uses my [Detectron2DeepSortPlus fork](https://github.com/jiafei1224/Detectron2DeepSortPlus/tree/master) to track the hand pose for segmentation in the RGB video data. 

Follow the [INSTALL.md](https://github.com/jiafei1224/Detectron2DeepSortPlus/blob/master/readme/INSTALL.md) for installation instructions, and download the trained models at [MODEL_ZOO.md](https://github.com/jiafei1224/Detectron2DeepSortPlus/blob/master/readme/MODEL_ZOO.md).
```bash
cd <install_dir>
git clone -b peract https://github.com/jiafei1224/Detectron2DeepSortPlus.git 

cd Detectron2DeepSortPlus
python yl2ds.py --input <PATH_TO_VIDEO> --tracker deepsort --weights <PATH_TO_WEIGHS> --out_vid <PATH_TO_OUTPUT_VIDEO> --device 'cuda:0'
```


#### 2. Segment Anything
AR2-D2 use my [Segment Anything](https://github.com/jiafei1224/segment-anything) for generating the segmented masks for human hand.

Follow the instructions in the SAM repo to install.
```bash
cd <install_dir>
git clone -b peract https://github.com/jiafei1224/segment-anything.git

cd segment_anything
python find_mask.py
```

#### 3. Towards An End-to-End Framework for Flow-Guided Video Inpainting (E2FGVI)
AR2-D2 use my [E2FGVI](https://github.com/jiafei1224/E2FGVI) to do inpainting of the hand for the RGB video data.

Follow their instruction to install and setup. You can alternatively run with the (`E2FGVI_Verison.ipynb`).

```bash
cd <install_dir>
git clone https://github.com/jiafei1224/E2FGVI.git

conda env create -f environment.yml
conda activate e2fgvi
python test.py --model e2fgvi (or e2fgvi_hq) --video <PATH_TO_RGB_VIDEO> --mask <PATH_TO_GENERATED_MASK> --ckpt release_model/E2FGVI-CVPR22.pth (or release_model/E2FGVI-HQ-CVPR22.pth)

```

