function Sharpening() {
   return (
      <div>
	<h1>Aguçamento de Bordas</h1>
   <UploadImage onInputChange={handleInputChange} />
      <form onSubmit={submitForm}>
        <div>
          <label>Informe o valor t: </label>
          <input type="text" name="parameter"/>
        </div>
        <div>
          <label>Informe o valor k: </label>
          <input type="text" name="parameter"/>
        </div>
        <input type="submit" />
      </form>
      </div>
   )
}

export default Sharpening
