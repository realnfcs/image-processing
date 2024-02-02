function Geometric() {
  return (
    <div>
      <h1>Operações Geométricas</h1>
      <UploadImage onInputChange={handleInputChange} />
      <form onSubmit={submitForm}>
        <div>
          <label>Informe a operação: </label>
          <select name="operation">
            <option value="zoom in">Zoom in</option>
            <option value="zoom out">Zoom out</option>
            <option value="cisalhamento">Cisalhamento</option>
            <option value="rebatimento">Rebatimento</option>
            <option value="rotacao">Rotação</option>
          </select>
        </div>
        <div>
          <label>Informe o valor: </label>
          <input type="text" name="parameter"/>
        </div>
        <input type="submit" />
      </form>
    </div>
  );
}

export default Geometric;
