function Convolution() {
   return (
      <div>
	<h1>Convolução</h1>
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
   )
}

export default Convolution
