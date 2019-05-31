module NetworkMarkup exposing (Error(..), Fetched(..), get, mapSuccess)

import Http
import Mark
import Mark.Error


type Fetched success
    = Loading
    | Failure Error
    | Success success


type Error
    = HttpError Http.Error
    | MarkErrors (List Mark.Error.Error)


get : String -> Mark.Document success -> (Fetched success -> msg) -> Cmd msg
get url document toMsg =
    let
        fromStringResult strRes =
            case strRes of
                Ok markup ->
                    case Mark.compile document markup of
                        Mark.Success success ->
                            Success success

                        Mark.Failure errors ->
                            Failure (MarkErrors errors)

                        Mark.Almost { errors } ->
                            Failure (MarkErrors errors)

                Err httpError ->
                    Failure (HttpError httpError)
    in
    Http.get
        { url = "/codecember.emu"
        , expect = Http.expectString (fromStringResult >> toMsg)
        }


mapSuccess : (success1 -> success2) -> Fetched success1 -> Fetched success2
mapSuccess fn fetched =
    case fetched of
        Loading ->
            Loading

        Failure err ->
            Failure err

        Success success ->
            Success (fn success)
