export async function sendCourses(courses) {
    let response = await fetch('http://localhost:5000/schedule', {
        method: 'POST',
        body: JSON.stringify({
            'courses': courses
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        },
    })
    return (await response.json())
}