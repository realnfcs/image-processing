function IntensityTransformation() {
   return (
      <div>
	<h1>Transformações de Intensidade</h1>
   <UploadImage onInputChange={handleInputChange} />
      <form onSubmit={submitForm}>
        <div>
          <label>Informe a operação: </label>
          <select name="operation">
            <option value="negativo">Negativo</option>
            <option value="alargamento">Alargamento de contraste</option>
            <option value="limiarizacao">Limiarização</option>
            <option value="potencia">Transformação de potência</option>
            <option value="logaritmica">Transformação logarítmica</option>
          </select>
        </div>
        <div>
          <label>Informe o primeiro valor: </label>
          <input type="text" name="parameter"/>
        </div>
        <div>
          <label>Informe o segundo valor: </label>
          <input type="text" name="parameter"/>
        </div>
        <input type="submit" />
      </form>
      </div>
   )
}

export default IntensityTransformation
