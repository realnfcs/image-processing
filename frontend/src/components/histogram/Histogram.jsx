import { useEffect, useState } from "react";
import UploadImage from "../uploadImage/UploadImage.jsx";

function Histogram() {
  const [images, setImages] = useState();
  const [resImage, setResImage] = useState();

  useEffect(() => {
    console.log("resImage State: ", resImage);
  }, [resImage]);

  function handleInputChange(values) {
    console.log("values", values);
    setImages(values);
  }

  function submitForm(e) {
    e.preventDefault();

    const formData = new FormData(e.target);

    images.forEach((file, index) => {
      formData.append(`file${index + 1}`, file);
    });

    const payload = Object.fromEntries(formData)

    console.log(payload, images);

    fetch('http://localhost:5000/histogram', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.json())
    .then(data => {
      if (data && data.image) {
        fetch(`http://localhost:5000/images/${data.image}`)
        .then(response => { 
          return response.blob()
        })
        .then(blob => {
            const imageUrl = URL.createObjectURL(blob);
            return imageUrl
        })
        .then(image => setResImage(image))
        .catch(error => console.error('Erro ao carregar a nova imagem:', error));
      }
    })
    .catch(error => {
      console.log("erro", error)
    })
  }

  return (
    <div>
      <h1>Histogramas</h1>
      <UploadImage onInputChange={handleInputChange} />
      <form onSubmit={submitForm}>
        <div>
          <label>Informe a operação: </label>
          <select name="operation">
            <option value="expansao">Expansão de histograma</option>
            <option value="equalizacao">Equalização de histograma</option>
          </select>
        </div>
        <input type="submit" />
      </form>

      {resImage && (
        <img src={resImage} key={resImage} />
      )}

    </div>
  );
}

export default Histogram;
