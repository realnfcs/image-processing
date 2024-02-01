import { useState } from "react";
import UploadImage from "../uploadImage/UploadImage.jsx";

function Algebraic() {

   const [images, setImages] = useState()

   function handleInputChange(values) {
      setImages(values) 
   }

  function submitForm(e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const payload = Object.fromEntries(formData)

    console.log(payload, images);
  }

  return (
    <div>
      <h1>Operações Algébricas</h1>
      <UploadImage onInputChange={handleInputChange} />
      <form onSubmit={submitForm}>
        <div>
          <label>Informe a operação: </label>
          <select name="operation">
            <option value="dissolver uniforme">Dissolver Uniforme</option>
            <option value="dissolver cruzado">Dissolver Cruzado</option>
          </select>
        </div>
        <div>
          <label>Informe o valor t: </label>
          <input type="text" name="parameter"/>
        </div>
        <input type="submit" />
      </form>
    </div>
  );
}

export default Algebraic;
