def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.

    Each box is [x1, y1, x2, y2] with (x1, y1) top-left and
    (x2, y2) bottom-right. Returns IoU in [0.0, 1.0].
    """
    # Intersection rectangle
    x_left   = max(box_a[0], box_b[0])
    y_top    = max(box_a[1], box_b[1])
    x_right  = min(box_a[2], box_b[2])
    y_bottom = min(box_a[3], box_b[3])

    # No overlap on either axis
    if x_right <= x_left or y_bottom <= y_top:
        return 0.0

    intersect_area = (x_right - x_left) * (y_bottom - y_top)

    area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])
    union_area = area_a + area_b - intersect_area

    if union_area <= 0:
        return 0.0

    return intersect_area / union_area