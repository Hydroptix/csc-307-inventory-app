import React, { Component } from 'react'

class Form extends Component {
   initialState = {
      user: '',
      artist: '',
      title: '',
      genre: '',
      durMin: '',
      durSec: '',
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
      const { user, artist, title, genre, durMin, durSec } = this.state

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
	  <label htmlFor="genre">Genre</label>
          <input
            type="text"
            name="genre"
            id="genre"
            value={genre}
            onChange={this.handleChange} />
	  <label htmlFor="durMin">Minutes</label>
          <input
            type="text"
            name="durMin"
            id="durMin"
            value={durMin}
            onChange={this.handleChange} />
	  <label htmlFor="durSec">Seconds</label>
          <input
            type="text"
            name="durSec"
            id="durSec"
            value={durSec}
            onChange={this.handleChange} />
          <input type="button" value="Submit" onClick={this.submitForm} />
        </form>
      )
   }
}

export default Form
