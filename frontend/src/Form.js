import React, { Component } from 'react'

class Form extends Component {
   initialState = {
      title: '',
      songs: []
   }

   state = this.initialState

   handleChange = event => {
      const { name, value } = event.target

      this.setState({
         [name]: value,
      })
   }

   submitForm = () => {
      this.props.handleSubmit(this.state)
      this.setState(this.initialState)
   }

   render() {
      const { title } = this.state

      return (
        <form>
          <label htmlFor="title">Playlist Name</label>
          <input 
            type="text"
            name="title"
            id="title"
            value={title}
            onChange={this.handleChange} />
          <input type="button" value="Submit" onClick={this.submitForm} />
        </form>
      )
   }
}

export default Form
