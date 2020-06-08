import React from 'react'

// Table Header for songs in selected playlist
const TableHeader = () => {
  return (
    <thead>
    <tr>
      <th>Song ID</th>
      <th>Artist</th>
      <th>Title</th>
      <th>Genre</th>
      <th>Duration</th>
      <th>Cover Art</th>
    </tr>
    </thead>
  )
}

// Table Header for playlists
const TableHeader2 = () => {
  return (
    <thead>
    <tr>
      <th>Playlist Name</th>
    </tr>
    </thead>
  )
}

// Table Body for songs in selected playlist
const TableBody = props => {

  let rows = props.songData.map((row, index) => {

    console.log(props.showDelete)

    //Don't show the delete button if told not to
    let deleteElement = undefined
    if (props.showDelete) {
      deleteElement =
        <td>
          <button onClick={() => props.removeSong(row._id)}>Remove from Playlist</button>
        </td>
    }

    return (
      <tr key={index}>
        <td>{row._id}</td>
        <td>{row.artist}</td>
        <td>{row.title}</td>
        <td>{row.genre}</td>
        <td>{row.durMin}:{row.durSec}</td>
        <td>
          <img
            src={row.image}
            alt='new'
            width="100"
            height="100"
          />
        </td>
        <td>
          <button onClick={() => props.addSong(index)}>Add to Playlist</button>
        </td>
        {deleteElement}
      </tr>
    )
  })

  return <tbody>{rows}</tbody>
}

// Table Body for playlists
const TableBody2 = props => {

  const rows = props.playlistData.map((row, index) => {
    return (
      <tr key={index}>
        <td>{row.title}</td>
        <td>
          <button onClick={() => props.removePlaylist(index)}>Delete</button>
        </td>
        <td>
          <button onClick={() => props.selectPlaylist(index)}>Select</button>
        </td>
      </tr>
    )
  })

  return <tbody>{rows}</tbody>
}

const Table = props => {
  const { songData, playlistData, removeSong, removePlaylist, selectPlaylist, addSong, showDelete } = props

  return (
    <table>
      <TableHeader/>
      <TableBody songData={songData} removeSong={removeSong} addSong={addSong} showDelete={showDelete}/>
      <TableHeader2/>
      <TableBody2 playlistData={playlistData} removePlaylist={removePlaylist} selectPlaylist={selectPlaylist}/>
    </table>

  )
}

export default Table
