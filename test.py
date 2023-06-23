import PIL.Image
from huggingface_hub import hf_hub_download

from FBA_Matting.inference import inference
from FBA_Matting.networks.models import build_model

REPO_ID = "leonelhs/FBA-Matting"

weights = hf_hub_download(repo_id=REPO_ID, filename="FBA.pth")
model = build_model(weights)
model.eval().cpu()


def predict(image, trimap):
    fg, bg, alpha, composite = inference(model, image, trimap)
    PIL.Image.fromarray(fg).save("./examples/predictions/girl_fg.png")
    PIL.Image.fromarray(bg).save("./examples/predictions/girl_bg.png")
    PIL.Image.fromarray(alpha).save("examples/predictions/girl_alpha.png")
    PIL.Image.fromarray(composite).save("examples/predictions/girl_composite.png")


if __name__ == "__main__":
    img = "./examples/images/girl.png"
    tri = "./examples/trimaps/girl.png"
    predict(img, tri)
