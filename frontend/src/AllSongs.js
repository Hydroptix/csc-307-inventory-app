import React, { Component } from 'react'
import Table from './Table'
import Form from './Form'
import axios from 'axios'

class AllSongs extends Component {
  state = {
    characters: []
  }

  removeCharacter = index => {
    const { characters } = this.state

    axios.delete('http://localhost:5000/users/'.concat(characters[index].id))

    this.setState({
      characters: characters.filter((character, i) => {
        return i !== index
      }),
    })
  }

  handleSubmit = character => {
    this.makePostCall(character).then(callResult => {
      if (callResult.status === 201) {
        this.setState({ characters: [...this.state.characters, callResult.data] })
      }
    })
  }

  makePostCall (character) {
    return axios.post('http://localhost:5000/songs', character)
      .then(function (response) {
        console.log(response)
        return response
      })
      .catch(function (error) {
        console.log(error)
        return false
      })
  }

  render () {
    const { characters } = this.state

    return (
      <div className="container">
        <Table characterData={characters} removeCharacter={this.removeCharacter}/>
        <Form handleSubmit={this.handleSubmit}/>
      </div>
    )
  }

  componentDidMount () {
    axios.get('http://localhost:5000/songs').then(res => {
      const characters = res.data.songs
      this.setState({ characters })
    })
      .catch(function (error) {
        //Not handling the error. Just logging into the console.
        console.log(error)
      })
  }
}

export default AllSongs