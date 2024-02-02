function EdgeDetectention() {
   return (
      <div>
	<h1>Detecção de Bordas</h1>
   <UploadImage onInputChange={handleInputChange} />
      <form onSubmit={submitForm}>
        <div>
          <label>Informe o valor t: </label>
          <input type="text" name="parameter"/>
        </div>
        <input type="submit" />
      </form>
      </div>
   )
}

export default EdgeDetectention
