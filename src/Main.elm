module Main exposing (main)

import Browser exposing (document)
import Browser.Events
import Element exposing (..)
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
    , markup : String
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



-- INIT


init : Flags -> ( Model, Cmd Msg )
init { size, markup } =
    ( { size = size
      , markup = markup
      }
    , Cmd.none
    )



-- UPDATE


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        SetSize size ->
            ( { model | size = size }, Cmd.none )



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
    case Markup.parseDocument model.markup of
        Ok days ->
            column [ centerX ]
                [ el
                    [ Font.size 48
                    , Font.bold
                    , centerX
                    , paddingXY 0 50
                    ]
                    (text "CODECEMBER 2018")
                , column [ centerX ]
                    (List.map (dayElement layout model.size) days)
                ]

        Err [] ->
            text "There were errors but there are no errors..."

        Err (firstError :: _) ->
            html (Mark.Error.toHtml Mark.Error.Light firstError)


dayElement : Layout -> WindowSize -> Day Msg -> Element Msg
dayElement layout size day =
    let
        side =
            min size.width size.height

        title_ =
            el [ paddingXY 0 15 ] (dayTitle day.day day.name)

        currentImage =
            el [ centerX ] (image_ side day.currentImage)

        content =
            column [ width fill, padding 100 ]
                [ title_
                , day.description
                ]
    in
    case layout of
        Narrow ->
            column [ width fill ]
                [ content, currentImage ]

        Wide ->
            row [ width fill ]
                [ currentImage, content ]


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
