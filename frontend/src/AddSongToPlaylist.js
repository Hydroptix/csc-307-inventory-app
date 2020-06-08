import React, { Component } from 'react'
import querystring from 'querystring'
import PlaylistSelectTable from './PlaylistSelectTable'
import axios from 'axios'

class AddSongToPlaylist extends Component {
  state = {
    songId: 0,
    playlists: [],
    errorMessage: ''
  }

  makePostCallPlaylist (playlist) {
    return axios.post('http://localhost:5000/inv', playlist)

      .then(function (response) {
        console.log(response)
        return response
      })
      .catch(function (error) {
        console.log(error)
        return false
      })
  }

  updatePlaylist = index => {
    const { playlists } = this.state

    axios.get('http://localhost:5000/inv/'.concat(playlists[index]._id)).then(res => {
      const inventory = res.data
      let songId = this.state.songId

      if (inventory.songs.includes(songId)) {
        this.setState({
          errorMessage: 'That playlist already contains this song'
        })

      } else {

        inventory.songs.push(songId)
        console.log(inventory)
        let postRes = this.makePostCallPlaylist(inventory)

        console.log("made post request")

        this.props.history.push("/songs")

      }

    })

  }

  render () {
    const { playlists } = this.state
    console.log('Made it!')
    return (
      <div className="container">
        <strong style={{ color: 'red' }}>{this.state.errorMessage}</strong>
        <PlaylistSelectTable
          playlistData={playlists}
          selectPlaylist={this.updatePlaylist}
        />
      </div>
    )
  }

  componentDidMount () {
    const id = parseInt(new URLSearchParams(this.props.location.search).get('songid'))

    this.setState({
      songId: id
    })

    axios.get('http://localhost:5000/inv').then(res => {
      const playlists = res.data.inventories
      this.setState({ playlists })
    })
      .catch(function (error) {
        console.log(error)
      })
  }

}

export default AddSongToPlaylist