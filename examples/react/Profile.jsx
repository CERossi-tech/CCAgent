export default function Profile({user}) {
  return <div dangerouslySetInnerHTML={{__html: user.bio}} />
}
