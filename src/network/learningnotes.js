import { request } from "./request"

export function getLearningNotesMultidata() {
    return request({
        url: '/learningnotes/multidata',
    })
}