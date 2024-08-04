# AUTOGENERATED! DO NOT EDIT! File to edit: dog_vs_cat.ipynb.

# %% auto 0
__all__ = ['learn', 'categories', 'image', 'label', 'examples', 'intf', 'is_cat', 'classify_image']

# %% dog_vs_cat.ipynb 1
from fastai.vision.all import *
import gradio as gr

def is_cat(x):
    return x[0].isupper()

# %% dog_vs_cat.ipynb 3
learn = load_learner('test/model_catvdog.pkl')

# %% dog_vs_cat.ipynb 5
# labels = learn.dls.vocab
categories = ('Dog', 'Cat')
def classify_image(img):
    pred, pred_idx, probs = learn.predict(img)
    return dict(zip(categories, map(float, probs)))
classify_image(img)
# def predict(img):
#     img = PILImage.create(img)
#     pred, pred_idx, probs = learn.predict(img)
#     return {labels[i]: float(probs[i]) for i in range(len(labels))}

# %% dog_vs_cat.ipynb 6
# gr.Interface(fn=predict, inputs=gr.Image(width=512, height=512),
#              outputs=gr.Label(num_top_classes=3)).launch(share=True)
image = gr.Image(width=192, height=192)
label = gr.Label()
examples = ['../data/dog.jpg', '../data/dog2.jpg', '../data/cat.jpg', '../data/hotdog.jpg',
            '../data/cat2.jpg', '../data/cougarwoman.jpg']
intf = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
intf.launch(inline=False)
