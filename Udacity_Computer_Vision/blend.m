function result = blend(image, subimage, alpha)
    result = (alpha * image) + ((1 - alpha) * subimage);
end