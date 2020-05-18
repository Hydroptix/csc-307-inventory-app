import React, { Component } from 'react'

class Form extends Component {
   initialState = {
      user: '',
      artist: '',
      title: '',
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
      const { user, artist, title } = this.state

      return (
        <form>
          <label htmlFor="user">User</label>
          <input 
            type="text"
            name="user"
            id="user"
            value={user}
            onChange={this.handleChange} />
          <label htmlFor="artist">Artist</label>
          <input
            type="text"
            name="artist"
            id="artist"
            value={artist}
            onChange={this.handleChange} />
	  <label htmlFor="title">Title</label>
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
