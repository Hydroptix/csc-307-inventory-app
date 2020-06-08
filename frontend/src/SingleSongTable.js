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

// Table Body for songs in selected playlist
const TableBody = props => {

  let rows = props.songData.map((row, index) => {

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
      </tr>
    )
  })

  return <tbody>{rows}</tbody>
}

const SingleSongTable = props => {
  const { songData } = props

  return (
    <table>
      <TableHeader/>
      <TableBody songData={songData} />
    </table>

  )
}

export default SingleSongTable
