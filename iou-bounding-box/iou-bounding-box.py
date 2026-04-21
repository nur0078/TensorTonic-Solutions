def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    #area of given boxes
    area_a = abs(box_a[2] - box_a[0]) * abs(box_a[3]-box_a[1])
    area_b = abs(box_b[2] - box_b[0]) * abs(box_b[3] - box_b[1])
    
    #intersection
    x_left = max(box_a[0], box_b[0])
    y_top = max(box_a[1], box_b[1])
    x_right = min(box_a[2], box_b[2])
    y_bottom = min(box_a[3], box_b[3])

    width = abs(x_right - x_left)
    height = abs(y_top - y_bottom)

    #intersection area
    intersect_area = float (width * height)
    

    a_union_b = float (area_a + area_b - intersect_area)

    iou = intersect_area / a_union_b

    if x_left < x_right:
        return iou
    return 0.0
    pass