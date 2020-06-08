import React, { Component } from 'react'
import Table from './Table'
import Form from './Form'
import axios from 'axios'

class AllSongs extends Component {
  state = {
    songs: [],
    playlists: []
  }

  removeSong = index => {
    const { songs } = this.state

    axios.delete('http://localhost:5000/songs/'.concat(songs[index].id))

    this.setState({
      songs: songs.filter((song, i) => {

        return i !== index
      }),
    })
  }

  removePlaylist = index => {
    const { playlists } = this.state

    axios.delete('http://localhost:5000/inv/'.concat(playlists[index]._id))

    this.setState({
      playlists: playlists.filter((playlist, i) => {
        return i !== index
      }),
    })
  }

  handleSubmit = playlist => {
    this.makePostCallPlaylist(playlist).then(callResult => {
      if (callResult.status === 201) {
        this.setState({ playlists: [...this.state.playlists, callResult.data] })

      }
    })
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

  selectPlaylist = index => {
    const { playlists } = this.state

    console.log('Running select')

    this.setState({
      songs: []
    })

    //Need to preserve this so we can access the state from inside the map statement
    let thisComponent = this

    axios.get('http://localhost:5000/inv/'.concat(playlists[index]._id)).then(res => {
      const song_ids = res.data.songs

      song_ids.map((id) => {
        return axios.get('http://localhost:5000/songs/'.concat(String(id))).then(function (res) {
          thisComponent.setState({
            songs: [...thisComponent.state.songs, res.data]
          })
        })
      })
    })
  }


  addSongs = songindex, playlistindex => {
    axios.post('http://localhost:5000/inventories/'.concat(String
  }


  render () {
    const { songs } = this.state
    const { playlists } = this.state

    console.log(JSON.stringify(songs))

    return (
      <div className="container">
        <Table songData={songs}
               playlistData={playlists}
               removeSong={this.removeSong}
               removePlaylist={this.removePlaylist}
               selectPlaylist={this.selectPlaylist}
               addSong={this.addSong}/>

        <Form handleSubmit={this.handleSubmit}/>
      </div>
    )
  }

  componentDidMount () {
    axios.get('http://localhost:5000/songs').then(res => {
      const songs = res.data.songs
      this.setState({ songs })
    })
      .catch(function (error) {
        //Not handling the error. Just logging into the console.
        console.log(error)
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

export default AllSongs
