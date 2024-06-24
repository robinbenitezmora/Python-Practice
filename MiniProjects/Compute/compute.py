import numpy as np

def compute(GT_bbox, Pred_bbox():
    '''
    Args:
        GT_bbox: ground truth bounding box
        Pred_bbox: predicted bounding box
    Returns:
        IOU: Intersection over Union
    '''

    # Compute the intersection area
    ixmin = max(GT_bbox[0], Pred_bbox[0])
    iymin = max(GT_bbox[1], Pred_bbox[1])
    ixmax = min(GT_bbox[2], Pred_bbox[2])
    iymax = min(GT_bbox[3], Pred_bbox[3])
    iw = np.maximum(ixmax - ixmin + 1., 0.)
    ih = np.maximum(iymax - iymin + 1., 0.)
    area = iw * ih

    # Compute the area of both bounding boxes
    S1 = (Pred_bbox[2] - GT_bbox[0] + 1) * (Pred_bbox[3] - GT_bbox[1] + 1)
    S2 = (GT_bbox[2] - GT_bbox[0] + 1) * (GT_bbox[3] - GT_bbox[1] + 1)
    S = S1 + S2 - area

    # Compute the Intersection over Union
    IOU = area / S
    return

if __name__ == "__main__":
    pred_bbox = np.array([40, 40, 100, 100])
    gt_bbox = np.array([70, 80, 110, 130])
    print(compute(gt_bbox, pred_bbox))