function Filters() {
   return (
      <div>
	<h1>Filtros</h1>
   <UploadImage onInputChange={handleInputChange} />
      <form onSubmit={submitForm}>
        <div>
          <label>Informe a operação: </label>
          <select name="operation">
            <option value="media">Filtro de média</option>
            <option value="mediana">Filtro de mediana</option>
          </select>
        </div>
        <input type="submit" />
      </form>
      </div>
   )
}

export default Filters
