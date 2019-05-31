module Main exposing (main)

import Array exposing (Array)
import Browser exposing (document)
import Browser.Events
import Element exposing (..)
import Element.Events
import Element.Font as Font
import Element.Keyed as Keyed
import Html exposing (Html)
import Mark.Error
import Markup exposing (Day)
import Task


main : Program Flags Model Msg
main =
    document
        { init = init
        , update = update
        , view = view
        , subscriptions = subscriptions
        }



-- MODEL


type alias Model =
    { size : WindowSize
    , days : Result (List Mark.Error.Error) (Array Day)
    }


type alias WindowSize =
    { width : Int
    , height : Int
    }


type alias Flags =
    { size : WindowSize
    , markup : String
    }


type Msg
    = SetSize WindowSize
    | AdvanceImages Int



-- INIT


init : Flags -> ( Model, Cmd Msg )
init { size, markup } =
    ( { size = size
      , days = Markup.parseDocument markup |> Result.map Array.fromList
      }
    , Cmd.none
    )



-- UPDATE


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        SetSize size ->
            ( { model | size = size }, Cmd.none )

        AdvanceImages dayIndex ->
            case model.days of
                Ok days ->
                    ( { model | days = Ok (arrayUpdate dayIndex advanceImages days) }
                    , Cmd.none
                    )

                Err _ ->
                    ( model, Cmd.none )


arrayUpdate : Int -> (a -> a) -> Array a -> Array a
arrayUpdate idx upd arr =
    case Array.get idx arr of
        Nothing ->
            arr

        Just val ->
            Array.set idx (upd val) arr


advanceImages : Day -> Day
advanceImages day =
    let
        ( prev, curr, next ) =
            day.images

        newImages =
            case next of
                upNext :: future ->
                    ( prev ++ [ curr ], upNext, future )

                [] ->
                    case prev of
                        upNext :: future ->
                            ( [ curr ], upNext, future )

                        [] ->
                            ( [], curr, [] )
    in
    { day | images = newImages }



-- VIEW


view : Model -> Browser.Document Msg
view model =
    { title = ""
    , body = [ layout [] (body model) ]
    }


type Layout
    = Wide
    | Narrow


body : Model -> Element Msg
body model =
    let
        layout =
            if toFloat model.size.width / toFloat model.size.height > 1.3 then
                Wide

            else
                Narrow
    in
    case model.days of
        Ok days ->
            column [ centerX ]
                [ el
                    [ Font.size 48
                    , Font.bold
                    , centerX
                    , paddingXY 0 50
                    ]
                    (text "CODECEMBER 2018")
                , paragraph []
                    [ text "This year blah blah blah"
                    ]
                , column [ centerX ]
                    (List.indexedMap (dayElement layout model.size) (Array.toList days))
                ]

        Err [] ->
            text "There were errors but there are no errors..."

        Err (firstError :: _) ->
            html (Mark.Error.toHtml Mark.Error.Light firstError)


dayElement : Layout -> WindowSize -> Int -> Day -> Element Msg
dayElement layout size dayIndex day =
    let
        side =
            min size.width size.height

        title_ =
            el [ paddingXY 0 15 ] (dayTitle day.day day.name)

        ( _, currentImage, _ ) =
            day.images

        currentImageElement =
            el [ centerX, Element.Events.onClick (AdvanceImages dayIndex) ] (image_ side currentImage)

        content =
            column [ width fill, padding 100 ]
                [ title_
                , Element.map never day.description
                ]
    in
    case layout of
        Narrow ->
            column [ width fill ]
                [ content, currentImageElement ]

        Wide ->
            row [ width fill ]
                [ currentImageElement, content ]


dayTitle : Int -> String -> Element Msg
dayTitle day title_ =
    el
        [ onLeft (title (String.fromInt day ++ ". "))
        ]
        (title title_)


title : String -> Element Msg
title string =
    el [ Font.size 24, Font.bold ] (text string)


image_ : Int -> String -> Element Msg
image_ side src =
    image [ height (px side) ]
        { src = src, description = "" }



-- SUBSCRIPTIONS


subscriptions : Model -> Sub Msg
subscriptions model =
    Browser.Events.onResize (\wd ht -> SetSize { width = wd, height = ht })
