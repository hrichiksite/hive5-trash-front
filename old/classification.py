from huggingface_hub import from_pretrained_fastai

def label_func(x): return x.parent.name

learn = from_pretrained_fastai("hrichikm/Trash_classification")
