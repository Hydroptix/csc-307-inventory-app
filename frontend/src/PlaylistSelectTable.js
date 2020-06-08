import React from 'react'

// Table Header for playlists
const TableHeader = () => {
  return (
    <thead>
    <tr>
      <th>Playlist Name</th>
    </tr>
    </thead>
  )
}

// Table Body for playlists
const TableBody = props => {

  const rows = props.playlistData.map((row, index) => {
    return (
      <tr key={index}>
        <td>{row.title}</td>
        <td>
          <button onClick={() => props.selectPlaylist(index)}>Add</button>
        </td>
      </tr>
    )
  })

  return <tbody>{rows}</tbody>
}

const PlaylistSelectTable = props => {
  const { playlistData, selectPlaylist } = props

  return (
    <table>
      <TableHeader/>
      <TableBody playlistData={playlistData} selectPlaylist={selectPlaylist}/>
    </table>

  )
}

export default PlaylistSelectTable
