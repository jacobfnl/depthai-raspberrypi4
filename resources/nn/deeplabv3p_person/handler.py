import cv2
import numpy as np

from depthai_helpers.managers import Previews
from depthai_helpers.utils import to_tensor_result


def decode(nn_manager, packet):
    data = np.squeeze(to_tensor_result(packet)["Output/Transpose"])
    class_colors = [[0,0,0],  [0,255,0]]
    class_colors = np.asarray(class_colors, dtype=np.uint8)

    output_colors = np.take(class_colors, data, axis=0)
    return output_colors


def draw(nn_manager, data, frames):
    if len(data) == 0:
        return

    for name, frame in frames:
        if name in (Previews.color.name, Previews.nn_input.name):
            cv2.addWeighted(frame, 1, cv2.resize(data, frame.shape[0:2][::-1]), 0.2, 0, frame)
