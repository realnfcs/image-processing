function Histogram() {
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
      </div>
   )
}

export default Histogram
