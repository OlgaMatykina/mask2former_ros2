import torch

import numpy as np

import multiprocessing as mp

from detectron2.data import MetadataCatalog
from semseg.defaults import DefaultPredictor
from detectron2.config import get_cfg
from mask2former import add_maskformer2_config
from detectron2.projects.deeplab import add_deeplab_config
# from visualizer import ColorMode, Visualizer

# from torchvision.models.segmentation import fcn_resnet50


class SemanticSegmentator:

    def __init__(self, config_file):        
        cfg = get_cfg()
        add_deeplab_config(cfg)
        add_maskformer2_config(cfg)
        cfg.merge_from_file(config_file)
        self.cpu_device = torch.device("cpu")
        cfg.freeze()
        print('INIT')
        self.predictor = DefaultPredictor(cfg)


    def inference(self, image):
        
        # batch = SemanticSegmentator.to_tensor(image)
        image = image[:, :, ::-1]

        probs = self.predictor(image, 'semantic')["sem_seg"]
        # print(probs)

        # probs = torch.softmax(logits['aux'][0], 0)
        segmentation = probs.argmax(dim=0) # * (probs.max(dim=0).values > treshold)
        # print(segmentation)
        new_cats_dict = {
            0: 0,    # 'Bird'
            1: 0,    # 'Ground Animal'
            2: 0,    # 'Curb'
            3: 0,    # 'Fence'
            4: 0,    # 'Guard Rail'
            5: 0,    # 'Barrier'
            6: 0,    # 'Wall'
            7: 0,    # 'Bike Lane'
            8: 3,    # 'Crosswalk - Plain'
            9: 0,    # 'Curb Cut'
            10: 3,   # 'Parking'
            11: 0,   # 'Pedestrian Area'
            12: 0,   # 'Rail Track'
            13: 3,   # 'Road'
            14: 3,   # 'Service Lane'
            15: 0,   # 'Sidewalk'
            16: 0,   # 'Bridge'
            17: 0,   # 'Building'
            18: 0,   # 'Tunnel'
            19: 2,   # 'Person'
            20: 2,   # 'Bicyclist'
            21: 2,   # 'Motorcyclist'
            22: 2,   # 'Other Rider'
            23: 3,   # 'Lane Marking - Crosswalk'
            24: 3,   # 'Lane Marking - General'
            25: 0,   # 'Mountain'
            26: 0,   # 'Sand'
            27: 0,   # 'Sky'
            28: 0,   # 'Snow'
            29: 0,   # 'Terrain'
            30: 0,   # 'Vegetation'
            31: 0,   # 'Water'
            32: 0,   # 'Banner'
            33: 2,   # 'Bench'
            34: 0,   # 'Bike Rack'
            35: 0,   # 'Billboard'
            36: 3,   # 'Catch Basin'
            37: 0,   # 'CCTV Camera'
            38: 2,   # 'Fire Hydrant'
            39: 0,   # 'Junction Box'
            40: 0,   # 'Mailbox'
            41: 3,   # 'Manhole'
            42: 0,   # 'Phone Booth'
            43: 1,   # 'Pothole'
            44: 0,   # 'Street Light'
            45: 0,   # 'Pole'
            46: 0,   # 'Traffic Sign Frame'
            47: 0,   # 'Utility Pole'
            48: 0,   # 'Traffic Light'
            49: 0,   # 'Traffic Sign (Back)'
            50: 0,   # 'Traffic Sign (Front)'
            51: 0,   # 'Trash Can'
            52: 2,   # 'Bicycle'
            53: 2,   # 'Boat'
            54: 2,   # 'Bus'
            55: 2,   # 'Car'
            56: 2,   # 'Caravan'
            57: 2,   # 'Motorcycle'
            58: 2,   # 'On Rails'
            59: 2,   # 'Other Vehicle'
            60: 2,   # 'Trailer'
            61: 2,   # 'Truck'
            62: 2,   # 'Wheeled Slow'
            63: 0,   # 'Car Mount'
            64: 2,   # 'Ego Vehicle'
            65: 0    # 'Unlabeled'
        }


        keys = np.array(list(new_cats_dict.keys()))
        values = np.array(list(new_cats_dict.values()))

        # Создаем новый массив с теми же размерами, что и исходный
        segmentation = SemanticSegmentator.to_ndarray(segmentation)
        road_mask = segmentation.copy()

        # Используем numpy для замены значений
        for key, value in zip(keys, values):
            road_mask[segmentation == key] = value


        return road_mask


    # @staticmethod
    # def to_tensor(image : np.ndarray):
    #     image_tensor = torch.Tensor(image.copy()).float() / 255
    #     mean = torch.Tensor([0.485, 0.456, 0.406])
    #     std = torch.Tensor([0.229, 0.224, 0.225])

    #     if torch.cuda.is_available():
    #         image_tensor = image_tensor.cuda()
    #         mean = mean.cuda()
    #         std = std.cuda()

    #     image_tensor = (image_tensor - mean) / std
    #     image_tensor = image_tensor.permute(2, 0, 1)

    #     batch = image_tensor.unsqueeze(0)

    #     return batch


    @staticmethod
    def to_ndarray(segmentation : torch.Tensor):
        return segmentation.cpu().numpy().astype(np.uint8)
    

    @staticmethod
    def colorize(segmentation : np.ndarray):
        # pallete = np.array([
        #     [255,255,255], #'unlabeled' : none
        #     [255,0,0], #'firehose' : red
        #     [255,165,0], #'hose' : orange
        #     [0,0,255], #'waste' : blue
        #     [255,255,0], #'puddle' : yellow
        #     [0,255,255], #'breakroad' : aqua
        #     [255,0,255], #'sidewalk' : magenta
        #     [0,128,0], #'terrain': green
        #     [250,128,114] #'road' : salmon
        # ], dtype=np.uint8)
        pallete = np.array([
            [255,255,255], #'unlabeled' : none
            [255,0,0], #'firehose' : red
            [255,165,0], #'hose' : orange
            [0,0,255], #'waste' : blue
            [255,255,0], #'puddle' : yellow
            [0,255,255], #'breakroad' : aqua
            [255,0,255], #'sidewalk' : magenta
            [0,128,0], #'terrain': green
            [127,72,41], #'vegetation': brown
            [250,128,114] #'road' : salmon
        ], dtype=np.uint8)

        segmentation_color = pallete[segmentation]

        return segmentation_color



# class VisualizationDemo(object):
#     def __init__(self, cfg, instance_mode=ColorMode.IMAGE, parallel=False):
#         """
#         Args:
#             cfg (CfgNode):
#             instance_mode (ColorMode):
#             parallel (bool): whether to run the model in different processes from visualization.
#                 Useful since the visualization logic can be slow.
#         """
#         self.metadata = MetadataCatalog.get(
#             cfg.DATASETS.TEST_PANOPTIC[0] if len(cfg.DATASETS.TEST_PANOPTIC) else "__unused"
#         )
#         if 'cityscapes_fine_sem_seg_val' in cfg.DATASETS.TEST_PANOPTIC[0]:
#             from cityscapesscripts.helpers.labels import labels
#             stuff_colors = [k.color for k in labels if k.trainId != 255]
#             self.metadata = self.metadata.set(stuff_colors=stuff_colors)
#         self.cpu_device = torch.device("cpu")
#         self.instance_mode = instance_mode

#         self.parallel = parallel
#         if parallel:
#             num_gpu = torch.cuda.device_count()
#             self.predictor = AsyncPredictor(cfg, num_gpus=num_gpu)
#         else:
#             self.predictor = DefaultPredictor(cfg)

#     def run_on_image(self, image, task):
#         """
#         Args:
#             image (np.ndarray): an image of shape (H, W, C) (in BGR order).
#                 This is the format used by OpenCV.
#         Returns:
#             predictions (dict): the output of the model.
#             vis_output (VisImage): the visualized image output.
#         """
#         vis_output = None
#         # Convert image from OpenCV BGR format to Matplotlib RGB format.
#         image = image[:, :, ::-1]
#         vis_output = {}
        
#         if task == 'panoptic':
#             visualizer = Visualizer(image, metadata=self.metadata, instance_mode=ColorMode.IMAGE)
#             predictions = self.predictor(image, task)
#             panoptic_seg, segments_info = predictions["panoptic_seg"]
#             vis_output['panoptic_inference'] = visualizer.draw_panoptic_seg_predictions(
#             panoptic_seg.to(self.cpu_device), segments_info, alpha=0.7
#         )

#         if task == 'panoptic' or task == 'semantic':
#             visualizer = Visualizer(image, metadata=self.metadata, instance_mode=ColorMode.IMAGE_BW)
#             predictions = self.predictor(image, task)
#             vis_output['semantic_inference'] = visualizer.draw_sem_seg(
#                 predictions["sem_seg"].argmax(dim=0).to(self.cpu_device), alpha=0.7
#             )

#         if task == 'panoptic' or task == 'instance':
#             visualizer = Visualizer(image, metadata=self.metadata, instance_mode=ColorMode.IMAGE_BW)
#             predictions = self.predictor(image, task)
#             instances = predictions["instances"].to(self.cpu_device)
#             vis_output['instance_inference'] = visualizer.draw_instance_predictions(predictions=instances, alpha=1)

#         return predictions, vis_output
